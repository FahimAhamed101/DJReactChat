from rest_framework import serializers
from .models import Server, Channel, Category


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = "__all__"



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields = "__all__"
        

class SeverSerializer(serializers.ModelSerializer):

    """
    Here, Channel data serialized and added to server, because they have a Foreign key relationship.
    If, there is no relationship, then this gives error.
    This can only be done iff there is a relationship between two models
    """
    channel_server = ChannelSerializer(many=True)
    category = serializers.StringRelatedField()

    # adding new field to server instance and should apecify a method accociate with SerializerMethodField
    num_members = serializers.SerializerMethodField(method_name='get_num_members')

    def get_num_members(self, obj):
        # self => refers to the instance of the serializer itself
        # obj  => refers to the individual object being serialized(instance of the model being serialized)
        if hasattr(obj, "num_members"):
            return obj.num_members
        else:
            return None

    class Meta:
        model = Server
        exclude = ("member",)

    """
    1. Purpose: Customizes how Server model instances are represented during serialization.
    2. Method Definition: Defined within the SeverSerializer class.
    3. Parameters: Takes self (serializer instance) and instance (individual object being serialized).
    4. Functionality: Calls the superclass method to delegate representation of the instance.
    5. Customization: Optional; can add custom logic to modify representation if needed. In this example, it delegates   without modifications
    
    def to_representation(self, instance):
         return super().to_representation(instance) 
    """
    

    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        num_members = self.context.get("num_members")
        if not num_members:
            """
            The None parameter in data.pop("num_members", None) acts as a default value returned if the key "num_members" is not found in the data dictionary.
            """
            data.pop("num_members", None)
        return data
    
    """
    1. Purpose: Customizes the representation of the serialized data for a Server instance.
    2. Method Definition: Defined within the SeverSerializer class.
    3. Parameters: Takes self (serializer instance) and instance (individual object being serialized).

    4. Functionality:

        => Calls the superclass method to retrieve the default representation of the instance.
        => Checks if num_members is present in the context.
        => If num_members is not present, removes the num_members field from the serialized data.
           Returns the modified data.
        => Customization: Conditional removal of num_members field based on the context
    """

    





"""

class SeverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = "__all__"

1. Importing Necessary Modules:

from rest_framework import serializers: This line imports the serializers module from the Django REST Framework. Serializers are classes that help with the conversion of complex data types, such as Django model instances, into native Python datatypes, which can then be easily rendered into JSON, XML, or other content types.
from .models import Server, Category: This imports the Server and Category models from your Django application. These models represent your database tables and are what you'll be serializing with the serializer.

2. Serializer Class Definition:

class ServerSerializer(serializers.ModelSerializer):: This line defines a serializer class named ServerSerializer. In Django REST Framework, serializers are Python classes that inherit from serializers.Serializer or one of its subclasses. Here, ModelSerializer is a subclass tailored for working with Django models. It provides a shortcut for automatically creating serializers based on Django models.

3. Meta Class Usage:

class Meta:: This is a nested class within ServerSerializer that provides metadata for the serializer.

    => model = Server: Inside the Meta class, model = Server indicates which Django model the serializer is associated with. In this case, it's associated with the Server model.

    => fields = "__all__": This line specifies which fields from the associated model should be included in the serialized output. "__all__" is a special value that tells Django to include all fields of the model in the serialization. Alternatively, you could specify a tuple of field names if you only wanted to include specific fields.

In summary, the ServerSerializer class is a Django REST Framework serializer specifically designed to work with instances of the Server model. It automatically generates serialization logic based on the model's fields, allowing you to easily convert Server model instances into JSON format and vice versa. This is particularly useful for building APIs where you need to serialize/deserialize data to communicate between the client and server.

"""    