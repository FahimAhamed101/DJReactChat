import { Box, useTheme } from "@mui/material";
// import api from "../api";
// import { useEffect, useState } from "react";
// import useAxiosWithInterceptor from "../helpers/jwt_interceptor";
// import ExploreCategories from "../components/SecondaryDraw/ExploreCategories";
import React from "react";
//////////////////////////////////////////////////////////

type SecondaryDrawProps = {
  children: React.ReactNode;
};

//////////////////////////////////////////////////////////
const SecondaryDraw = ({ children }: SecondaryDrawProps) => {
  const theme = useTheme();
  // const jwtAxos = useAxiosWithInterceptor();

  /////////////////////////////////////////////////////////
  return (
    <Box
      sx={{
        minWidth: `${theme.secondaryDraw.width}px`,
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        borderRight: `1px solid ${theme.palette.divider}`,
        display: { xs: "none", sm: "block" },
        marginTop: `${theme.primaryAppBar.height}px`,
        overflow: "auto",
      }}
    >
      {children}
    </Box>
  );
};

export default SecondaryDraw;