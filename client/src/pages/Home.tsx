import { Box } from "@mui/material";
import PrimaryAppBar from "../templates_/PrimaryAppBar";
import PrimaryDraw from "../templates_/PrimaryDraw";
import SecondaryDraw from "../templates_/SecondaryDraw";

import PopularChannels from "../components/PrimaryDraw/PopularChannels";


//////////////////////////////////////////////////////

/////////////////////////////////////////////
const Home = () => {
  ///////////////////////////////////
  return (
    <Box sx={{ display: "flex" }}>
      <PrimaryAppBar />
      <PrimaryDraw>
        <PopularChannels isDrawerOpen={true} />
      </PrimaryDraw>
      
      
    </Box>
  );
};

export default Home;