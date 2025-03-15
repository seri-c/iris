import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Logo from '../assets/logo.png';
import Container from '@mui/material/Container';
import React from 'react';
import HomeIcon from '@mui/icons-material/Home';
import CollectionsBookmarkIcon from '@mui/icons-material/CollectionsBookmark';
import ShuffleIcon from '@mui/icons-material/Shuffle';
import { Box, IconButton, styled, useScrollTrigger } from '@mui/material';

interface Props {
  children?: React.ReactElement<{ elevation?: number }>;
}


function ElevationScroll(props: Props) {
  const { children } = props;

  const trigger = useScrollTrigger({
    disableHysteresis: true,
    threshold: 0,
  });

  return children
    ? React.cloneElement(children, {
      elevation: trigger ? 4 : 0,
    })
    : null;
}




export default function ElevateAppBar(props: Props) {
  return (
    <>
      {/* <CssBaseline /> */}
      <ElevationScroll {...props}>
        <AppBar sx={{ bgcolor: "white" }}>
          <Toolbar>
            <Box display='flex' flexGrow={1}>
              <img src={Logo} width={60} alt="irisLogo" />
              <Typography variant="h4" color="primary" fontWeight='bold' component="div">
                Iris
              </Typography>
            </Box>

          
            <IconButton aria-label="home" color="primary" >
              <HomeIcon fontSize='large'/>
            </IconButton>
            <IconButton aria-label="shuffle" color="primary">
              <ShuffleIcon fontSize='large'/>
            </IconButton>
            
            <IconButton aria-label="bookmarks" color="primary">
              <CollectionsBookmarkIcon fontSize='large'/>
            </IconButton>
          </Toolbar>
        </AppBar>
      </ElevationScroll>
      <Toolbar />
      <Container>

      </Container>
    </>
  );
}