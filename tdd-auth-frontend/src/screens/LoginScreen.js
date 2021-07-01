import React, { useEffect, useState } from "react";
import { login } from "../services/AuthService";
import StorageService from "../services/StorageService";

const LoginScreen = () => {
  const url = window.location.href;
  const redir = (/\?redir=([\s\S]*)/.exec(url) || [])[1];
  const [token, setToken] = useState(StorageService.getAccessToken());
  const [shouldRedirect, setShouldRedirect] = useState(!!token);

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });
  const handleChange = (e) => {
    setFormData({
      ...formData,

      // Trimming any whitespace
      [e.target.name]: e.target.value.trim(),
    });
  };

  const [response, setResponse] = useState({ result: null, error: null });

  useEffect(() => {
    setShouldRedirect(!!token);
  }, [token, shouldRedirect]);

  const onSubmit = (e) => {
    // TODO: add form validation
    e.preventDefault();
    login(formData)
      .then((r) => {
        setToken(r.access);
        setShouldRedirect(!!token);
        setResponse({ ...response, result: r });
      })
      .catch((e) => setResponse({ ...response, error: e }));
  };
  if (shouldRedirect && redir) {
    window.location = `${redir}?token=${token}`;
    return <div>Redirecting...</div>;
  } else {
    console.log(shouldRedirect, token, redir);
  }
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
            return JSON.stringify(response.error[keys[0]]);
          })()}
        </div>
      )}
      {response.result && <div>Successfull.</div>}
    </div>
  );
};

export default LoginScreen;
