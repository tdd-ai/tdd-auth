import "./App.css";
import { Switch, Route, Link, HashRouter } from "react-router-dom";
import { AUTH_ROUTES } from "./constants/Routes";
import LoginScreen from "./screens/LoginScreen";
import SignUpScreen from "./screens/SignUpScreen";

function App() {
  return (
    <HashRouter>
      <div className="App">
        <nav className="navbar navbar-expand-lg navbar-light fixed-top">
          <div className="container">
            <Link className="navbar-brand" to={"/login"}>
              Turkish Data Depository
            </Link>
            <div className="collapse navbar-collapse" id="navbarTogglerDemo02">
              <ul className="navbar-nav ml-auto">
                <li className="nav-item">
                  <Link className="nav-link" to={"/login"}>
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to={"/signup"}>
                    Sign Up
                  </Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <div className="auth-wrapper">
          <div className="auth-inner">
            <Switch>
              <Route exact path="/" component={LoginScreen} />
              <Route path="/login" component={LoginScreen} />
              <Route path="/signup" component={SignUpScreen} />
              <Route path="/forgot-password" component={() => {
                window.location.href = AUTH_ROUTES.FORGOT_PASSWORD
              }} />
            </Switch>
          </div>
        </div>
      </div>
    </HashRouter>
  );
}

export default App;
