import { Box, IconButton, useTheme } from "@mui/material";
import ChevronLeftIcon from "@mui/icons-material/ChevronLeft";
import ChevronRightIcon from "@mui/icons-material/ChevronRight";

type Props = {
  isDrawerOpen: boolean;
  handleDrawerOpen: () => void;
  handleDrawerClose: () => void;
};

const DrawToggle: React.FC<Props> = ({
  isDrawerOpen,
  handleDrawerOpen,
  handleDrawerClose,
}) => {
  const theme = useTheme();
  return (
    <Box
      sx={{
        height: "50px",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        position: "sticky",
        top: 0,
        zIndex: 999,
        backgroundColor: theme.palette.background.default,
      }}
    >
      <IconButton onClick={isDrawerOpen ? handleDrawerClose : handleDrawerOpen}>
        {isDrawerOpen ? <ChevronLeftIcon /> : <ChevronRightIcon />}
      </IconButton>
    </Box>
  );
};

export default DrawToggle;