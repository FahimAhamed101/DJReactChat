import { createTheme, responsiveFontSizes } from "@mui/material";

declare module "@mui/material/styles" {
  interface Theme {
    primaryAppBar: {
      height: number;
    };
    primaryDraw: {
      width: number;
      closedWidth: number;
    };
    secondaryDraw: {
      width: number;
    };
  }

  interface ThemeOptions {
    primaryAppBar?: {
      height?: number;
    };
    primaryDraw?: {
      width?: number;
      closedWidth?: number;
    };
    secondaryDraw?: {
      width?: number;
    };
  }
}

export const createMuiTheme = (mode: "light" | "dark") => {
  let theme = createTheme({
    primaryAppBar: {
      height: 50,
    },
    primaryDraw: {
      width: 240,
      closedWidth: 70,
    },
    secondaryDraw: {
      width: 240,
    },
    palette: {
      mode: mode,
    },
    components: {
      MuiAppBar: {
        defaultProps: {
          color: "default",
          elevation: 0,
        },
      },
    },
    typography: {
      fontFamily: ["IBM Plex Sans", "sans-serif"].join(","),
      body1: {
        fontWeight: 500,
      },
    },
  });
  theme = responsiveFontSizes(theme);
  return theme;
};

export default createMuiTheme;