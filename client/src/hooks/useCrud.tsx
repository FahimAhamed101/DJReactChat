import useAxiosWithInterceptor from "../helpers/jwt_interceptor";
import { BASE_URL } from "../api";
import { useState } from "react";
import axios, { AxiosError } from "axios";
/////////////////////////////////////

interface IuseCRUD<T> {
  dataCRUD: T[];
  fetchData: () => Promise<void>;
  error: Error | null;
  isLoading: boolean;
}

const useCrud = <T,>(initialData: T[], apiURL: string): IuseCRUD<T> => {
  const jwtAxios = useAxiosWithInterceptor();
  const [dataCRUD, setDataCRUD] = useState<T[]>(initialData);
  const [error, setError] = useState<Error | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const fetchData = async () => {
    setIsLoading(true);
    try {
      const response = await jwtAxios.get(`${BASE_URL}${apiURL}`, {});
      const data = response.data;
      setDataCRUD(data);
      setIsLoading(false);
      setError(null);
      return data;
    } catch (error: unknown) {
      if (axios.isAxiosError(error)) {
        const axiosError = error as AxiosError;
        if (axiosError.response && axiosError.response.status === 400) {
          setError(new Error("400"));
        }
      }
      setIsLoading(false);
      throw error;
    }
  };
  return { fetchData, dataCRUD, error, isLoading };
};
export default useCrud;