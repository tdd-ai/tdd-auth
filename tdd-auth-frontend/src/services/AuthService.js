import { AUTH_ROUTES } from "../constants/Routes";
import StorageService from "./StorageService";

/**
 * Sign up for tdd auth
 * @param {*} param0 body of the sign up
 * Nullable fields
 * @param {string?} param0.last_name
 * @param {string?} param0.affiliation
 */
export const signUp = async ({
  email,
  first_name,
  last_name,
  affiliation,
  password,
}) => {
  let result = await fetch(AUTH_ROUTES.SIGN_UP, {
    method: "POST",
    url: AUTH_ROUTES.SIGN_UP,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      first_name,
      last_name,
      affiliation,
      password,
    }),
  });
  let status = result.status;
  if (status < 400) {
    let resText = await result.text();
    return resText;
  }
  let resJson = await result.json();
  throw resJson;
};

/**
 * Login for tdd auth
 * @param {string?} param0.email
 * @param {string?} param0.password
 */
export const login = async ({ email, password }) => {
  let result = await fetch(AUTH_ROUTES.LOGIN, {
    method: "POST",
    url: AUTH_ROUTES.LOGIN,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });
  let status = result.status;
  if (status < 400) {
    let resJson = await result.json();
    StorageService.saveAccessToken(resJson["access"]);
    StorageService.saveRefreshToken(resJson["refresh"]);
    return resJson;
  }
  let resJson = await result.json();
  throw resJson;
};

export const forgot_password = async ({email}) => {
  let result = await fetch(AUTH_ROUTES.FORGOT_PASSWORD, {
    method: "POST",
    url: AUTH_ROUTES.FORGOT_PASSWORD,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email
    }),
  });
  let status = result.status;
  if (status < 400) {
    let resJson = await result.json();
    return resJson;
  }
  let resJson = await result.json();
  throw resJson;
};