import {
    AppBar,
    Link,
    Toolbar,
    Typography,
    useTheme,
    Box,
    IconButton,
    Drawer,
    useMediaQuery,
  } from "@mui/material";
  import MenuIcon from "@mui/icons-material/Menu";
  import { useState } from "react";

  /////////////////////////////////////////////////////////////////////
  
  const PrimaryAppBar = () => {
    const theme = useTheme();
    const [isOpenSideMenu, setIsOpenSideMenu] = useState(false);
    const isSmallScreen = useMediaQuery(theme.breakpoints.down("sm"));
  
    ////////////////////////////////////////////////////////////////////
    return (
      <AppBar
        sx={{
          zIndex: (theme) => theme.zIndex.drawer + 2,
          backgroundColor: theme.palette.background.default,
          borderBottom: `1px solid ${theme.palette.divider}`,
        }}
      >
        <Toolbar
          variant="dense"
          sx={{
            height: theme.primaryAppBar.height,
            minHeight: theme.primaryAppBar.height,
          }}
        >
          <Box
            sx={{
              display: { xs: "block", sm: "none" },
              ...(isOpenSideMenu && { color: "cornflowerblue" }),
            }}
          >
            <IconButton
              color="inherit"
              aria-label="open drawer"
              edge="start"
              sx={{ marginRight: "5px", cursor: "pointer" }}
              onClick={() => setIsOpenSideMenu((prev) => !prev)}
            >
              <MenuIcon />
            </IconButton>
          </Box>
  
          <Drawer
            anchor="left"
            open={isOpenSideMenu && isSmallScreen}
            onClose={() => setIsOpenSideMenu((prev) => !prev)}
          >
            <Box
              sx={{
                paddingTop: `${theme.primaryAppBar.height}px`,
                minWidth: 200,
              }}
              role="presentation"
              onClick={() => setIsOpenSideMenu((prev) => !prev)}
              onKeyDown={() => setIsOpenSideMenu((prev) => !prev)}
            >

            </Box>
          </Drawer>
  
          <Link href="/" underline="none" color="inherit">
            <Typography
              variant="h5"
              noWrap
              component="div"
              sx={{ letterSpacing: "-0.5px", fontWeight: 700 }}
            >
              DJ
              <Typography
                variant="h6"
                noWrap
                component="span"
                sx={{ fontWeight: 400 }}
              >
                CHAT
              </Typography>
            </Typography>
          </Link>
          <Box sx={{ flexGrow: 1 }}></Box>
  
        </Toolbar>
      </AppBar>
    );
  };
  
  export default PrimaryAppBar;