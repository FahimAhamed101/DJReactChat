import { ThemeProvider, useMediaQuery } from "@mui/material";
import React, { useEffect, useMemo, useState } from "react";
import createMuiTheme from "./theme";
import { ColorModeContext } from "../context/DarkModeContext";
import Cookies from "js-cookie";
/////////////////////////////////////////////////////////////

interface ToggleColorModeProps {
  children: React.ReactNode;
}

const ToggleColorMode: React.FC<ToggleColorModeProps> = ({ children }) => {
  const prefersDarkMode = useMediaQuery("(prefers-color-scheme: dark)");
  const storedColorMode = Cookies.get("colorMode") as "light" | "dark";
  const defaultMode = storedColorMode || (prefersDarkMode ? "dark" : "light");
  const [mode, setMode] = useState<"light" | "dark">(defaultMode);

  const toggleColorMode = React.useCallback(() => {
    setMode((prevMode) => (prevMode === "dark" ? "light" : "dark"));
  }, []);

  useEffect(() => {
    Cookies.set("colorMode", mode);
  }, [mode]);

  const colorMode = useMemo(() => ({ toggleColorMode }), [toggleColorMode]);
  const theme = React.useMemo(() => createMuiTheme(mode || "light"), [mode]);

  return (
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>{children}</ThemeProvider>
    </ColorModeContext.Provider>
  );
};

export default ToggleColorMode;