import React from 'react';
import { Container, Navbar } from 'react-bootstrap';
import { ReactComponent as Logo } from '../images/logo.svg';
const navbarStyle = {
  backgroundColor: '#eeeeee',
};

const Header = (/*props*/ { title }) => {
  //const { title} = props;
  return (
    <Navbar style={navbarStyle} variant="light">
      <Container>
        <Logo alt={title} style={{ maxWidth: '14rem', maxHight: '2rem' }} />
      </Container>
    </Navbar>
  );
};
export default Header;
