import React, { useState } from "react";
import { login } from "../services/AuthService";

import { useQuery } from "../hooks";

const LoginScreen = () => {
  let query = useQuery();
  const redirectUrl = query.get("redir");

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const [response, setResponse] = useState({ result: null, error: null });

  const handleChange = (e) => {
    setFormData({
      ...formData,

      // Trimming any whitespace
      [e.target.name]: e.target.value.trim(),
    });
  };

  const redirectToUrl = (token) => {
    setTimeout(() => {
      window.location.assign(redirectUrl + `#/?token=${token}`);
    }, 1500);
  };

  const onSubmit = (e) => {
    // TODO: add form validation
    e.preventDefault();

    login(formData)
      .then((r) => {
        setResponse({ ...response, result: r });

        r?.access && redirectToUrl(r.access);
      })
      .catch((e) => setResponse({ ...response, error: e }));
  };
  return (
    <div>
      {!response.error && !response.result && (
        <form onSubmit={onSubmit}>
          <h3>Login</h3>

          <div className="form-group">
            <label>Email address</label>
            <input
              type="email"
              name="email"
              className="form-control"
              placeholder="Enter email"
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              name="password"
              className="form-control"
              placeholder="Enter password"
              onChange={handleChange}
            />
          </div>

          <button
            type="submit"
            className={
              formData.email && formData.password
                ? "btn btn-primary btn-block"
                : "disabled-btn btn btn-primary btn-block "
            }
            disabled={!formData.email || !formData.password}
          >
            Submit
          </button>
        </form>
      )}
      {response.error && (
        <div>
          ERROR:{" "}
          {(() => {
            let keys = Object.keys(response.error);
            return response.error[keys[0]];
          })()}
        </div>
      )}
      {redirectUrl && response.result?.access && (
        <div>Redirecting to {redirectUrl.split("?")[0]}</div>
      )}
    </div>
  );
};

export default LoginScreen;
