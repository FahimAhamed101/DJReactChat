import React from "react";

interface ColorModeProps {
  toggleColorMode: () => void;
}

export const ColorModeContext = React.createContext<ColorModeProps>({
  toggleColorMode: () => {},
});