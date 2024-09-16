import {
    List,
    ListItem,
    ListItemText,
    ListItemButton,
    ListItemIcon,
    Box,
    Typography,
  } from "@mui/material";
  import useCrud from "../../hooks/useCrud";
  import React, { useEffect } from "react";
  import ListItemAvatar from "@mui/material/ListItemAvatar";
  import Avatar from "@mui/material/Avatar";
  import { MEDIA_URL } from "../../api";
  import { Link } from "react-router-dom";
  ////////////////////////////////////////////////////////////////////
  
  type Props = {
    isDrawerOpen: boolean;
  };
  
  interface Server {
    id: number;
    name: string;
    category: string;
    icon: string;
  }
  
  ///////////////////////////////////////////////////////////////////
  const PopularChannels: React.FC<Props> = ({ isDrawerOpen }) => {
    const { fetchData, dataCRUD, error, isLoading } = useCrud<Server>(
      [],
      "/server/select/"
    );
  
    useEffect(() => {
      fetchData();
    }, []);
  
    // useEffect(() => {
    //   console.log(dataCRUD);
    // }, [dataCRUD]);
  
    //////////////////////////////////////////////////////////////
    return (
      <>
        <Box
          sx={{
            height: "50px",
            width: "100%",
            padding: "20px",
            display: "flex",
            alignItems: "center",
            flex: "1 1 100%",
          }}
        >
          <Typography
            sx={{
              display: isDrawerOpen ? "block" : "none",
              letterSpacing: "1px",
              fontWeight: 500,
            }}
          >
            Popular Channels
          </Typography>
        </Box>
        <List>
          {dataCRUD?.map((item) => (
            <ListItem
              sx={{ display: "block" }}
              dense={true}
              disablePadding
              key={item.id}
            >
              <Link
                to={`/server/${item.id}`}
                style={{ textDecoration: "none", color: "inherit" }}
              >
                <ListItemButton
                  sx={{
                    minHeight: 0,
                  }}
                >
                  <ListItemIcon sx={{ minWidth: 0, justifyContent: "center" }}>
                    <ListItemAvatar sx={{ minWidth: "50px" }}>
                      <Avatar
                        alt="server icon"
                        src={`${MEDIA_URL}${item.icon}`}
                      />
                    </ListItemAvatar>
                  </ListItemIcon>
                  <ListItemText
                    sx={{
                      opacity: isDrawerOpen ? 1 : 0,
                    }}
                    primaryTypographyProps={{
                      sx: {
                        textOverflow: "ellipsis",
                        overflow: "hidden",
                        whiteSpace: "nowrap",
                      },
                    }}
                    primary={
                      <Typography
                        variant="body2"
                        sx={{
                          fontWeight: 700,
                          lineHeight: 1.2,
                          textOverflow: "ellipsis",
                          overflow: "hidden",
                          fontSize: "17px",
                          textTransform: "capitalize",
                        }}
                      >
                        {item.name}
                      </Typography>
                    }
                    secondary={
                      <Typography
                        variant="body2"
                        sx={{
                          fontWeight: 500,
                          lineHeight: 1.2,
                          color: "textSecondary",
                          fontSize: "13px",
                        }}
                      >
                        {item.category}
                      </Typography>
                    }
                  />
                </ListItemButton>
              </Link>
            </ListItem>
          ))}
        </List>
      </>
    );
  };
  
  export default PopularChannels;