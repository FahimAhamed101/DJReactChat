import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import { CssBaseline } from "@mui/material";
import ToggleColorMode from "./theme/ToggleColorMode";
function App() {
  return (
    <ToggleColorMode>
        <CssBaseline />
    <Routes>

    <Route
      path="/"
      element={ <Home />}
    />
   
  </Routes>
  </ToggleColorMode>
  );
}

export default App;
