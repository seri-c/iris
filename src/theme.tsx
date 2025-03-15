import { createTheme } from '@mui/material/styles';

let theme = createTheme({
    typography: {
        fontFamily: [
          'Georgia',
          'Nunito',
          'Roboto',
          '"Helvetica Neue"',
          'Arial',
          'sans-serif'
        ].join(','),
      }
  });


export const AppTheme = createTheme(theme, {
  // Custom colors created with augmentColor go here
  palette: {
    primary: theme.palette.augmentColor({
      color: {
        main: '#EC5151',
      },
      name: 'primary',
    }),
  },
});

declare module "@mui/material/Button" {
    interface ButtonPropsColorOverrides {
      salmon: true;
    }
  }

  declare module "@mui/material/IconButton" {
    interface IconButtonPropsColorOverrides {
      salmon: true;
    }
  }
