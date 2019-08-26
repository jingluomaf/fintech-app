import React from "react";
import { connect } from "react-redux";
import { createStructuredSelector } from "reselect";

import CartIcon from "../cart-icon/cart-icon.component";
import CartDropdown from "../cart-dropdown/cart-dropdown.component";
import { selectCartHidden } from "../../redux/cart/cart.selectors";
import { selectCurrentUser } from "../../redux/user/user.selectors";
import { signOutStart } from "../../redux/user/user.actions";

import { ReactComponent as Logo } from "../../assets/crown.svg";

import {
  HeaderContainer,
  LogoContainer,
  OptionsContainer,
  OptionLink,
  OptionWeb
} from "./header.styles";

export const Header = ({ currentUser, hidden, signOutStart }) => (
  <HeaderContainer>
    <LogoContainer to="/">
      <Logo className="logo" />
    </LogoContainer>
    <OptionsContainer>
      <OptionWeb>
        <a
          href="http://localhost:8888"
          target="_blank"
          rel="noopener noreferrer"
        >
          JUPYTER
        </a>
      </OptionWeb>
      <OptionWeb>
        <a
          href="http://localhost:8088"
          target="_blank"
          rel="noopener noreferrer"
        >
          SUPERSET
        </a>
      </OptionWeb>
      <OptionWeb>
        <a
          href="http://localhost:8000"
          target="_blank"
          rel="noopener noreferrer"
        >
          DJANGO
        </a>
      </OptionWeb>
      <OptionWeb>
        <a
          href="http://localhost:8080"
          target="_blank"
          rel="noopener noreferrer"
        >
          PORTAINER
        </a>
      </OptionWeb>
      <OptionWeb>
        <a
          href="http://localhost:9000"
          target="_blank"
          rel="noopener noreferrer"
        >
          MINIO
        </a>
      </OptionWeb>
      <OptionWeb>
        <a
          href="http://localhost:8080"
          target="_blank"
          rel="noopener noreferrer"
        >
          AIRFLOW
        </a>
      </OptionWeb>
      <OptionLink to="/shop">SHOP</OptionLink>
      <OptionLink to="/shop">CONTACT</OptionLink>
      {currentUser ? (
        <OptionLink as="div" onClick={signOutStart}>
          SIGN OUT
        </OptionLink>
      ) : (
        <OptionLink to="/signin">SIGN IN</OptionLink>
      )}
      <CartIcon />
    </OptionsContainer>
    {hidden ? null : <CartDropdown />}
  </HeaderContainer>
);

const mapStateToProps = createStructuredSelector({
  currentUser: selectCurrentUser,
  hidden: selectCartHidden
});

const mapDispatchToProps = dispatch => ({
  signOutStart: () => dispatch(signOutStart())
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Header);
