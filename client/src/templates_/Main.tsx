import { Box, useTheme } from "@mui/material";
import React, { ReactNode } from "react";

type Props = {
  children: ReactNode;
};

const Main: React.FC<Props> = ({ children }) => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        flex: 1,
        // background: "lightblue",
        height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
        marginTop: `${theme.primaryAppBar.height}px`,
        overflow: "hidden",
      }}
    >
      {children}
    </Box>
  );
};

export default Main;