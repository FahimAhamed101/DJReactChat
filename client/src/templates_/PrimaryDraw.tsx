import { Box, styled, useMediaQuery, useTheme } from "@mui/material";
import React, { ReactNode, useEffect, useState } from "react";
import DrawToggle from "../components/PrimaryDraw/DrawToggle";
import MuiDrawer from "@mui/material/Drawer";
////////////////////////////////////////////

type Props = {
  children: ReactNode;
};

type ChildProps = {
  isDrawerOpen: boolean;
};

type ChildElement = React.ReactElement<ChildProps>;

//////////////////////////////
const PrimaryDraw: React.FC<Props> = ({ children }) => {
  const theme = useTheme();
  const below600 = useMediaQuery("(max-width: 599px)");
  const [isDrawerOpen, setIsDrawerOpen] = useState(!below600);

  useEffect(() => {
    setIsDrawerOpen(!below600);
  }, [below600]);

  const handleDrawerOpen = () => {
    setIsDrawerOpen(true);
  };

  const handleDrawerClose = () => {
    setIsDrawerOpen(false);
  };

  const openedMixin = () => ({
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    overflowX: "hidden",
  });

  const closedMixin = () => ({
    transition: theme.transitions.create("width", {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
    overflowX: "hidden",
    width: theme.primaryDraw.closedWidth,
  });

  const Drawer = styled(MuiDrawer)({
    position: "relative", //imp
    width: 240, //drawer width
    "& .MuiDrawer-paper": {
      width: 240, //drawer width
      position: "absolute", //imp
      transition: "none !important"
    }
})

  ///////////////////////////////////////
  return (
    <Drawer
      open={isDrawerOpen}
      variant={below600 ? "temporary" : "permanent"}
      PaperProps={{
        sx: {
          marginTop: `${theme.primaryAppBar.height}px`,
          height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
          width: `${theme.primaryDraw.width}px`,
        },
      }}
    >
      <Box>
        <Box
          sx={{
            position: "absolute",
            top: 0,
            ...(isDrawerOpen ? { right: 0 } : { left: 0 }),
            padding: 0,
            ...(isDrawerOpen ? { width: "auto" } : { width: "100%" }),
          }}
        >
          <DrawToggle
            isDrawerOpen={isDrawerOpen}
            handleDrawerOpen={handleDrawerOpen}
            handleDrawerClose={handleDrawerClose}
          />
        </Box>
        {React.Children.map(children, (child) => {
          return React.isValidElement(child)
            ? React.cloneElement(child as ChildElement, { isDrawerOpen })
            : child;
        })}
      </Box>
    </Drawer>
  );
};

export default PrimaryDraw;