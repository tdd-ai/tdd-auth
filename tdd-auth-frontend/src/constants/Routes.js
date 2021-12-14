const AUTH_BASE = "https://auth-api.tdd.ai";
const TEST_BASE = "http://localhost:8000";
export const AUTH_ROUTES = Object.freeze({
  SIGN_UP: AUTH_BASE + "/signup/",
  LOGIN: AUTH_BASE + "/api/token/",
  FORGOT_PASSWORD: AUTH_BASE + "/password-reset/",
});
