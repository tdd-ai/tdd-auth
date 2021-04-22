import React, { useState } from "react";
import { login } from "../services/AuthService";

const LoginScreen = () => {
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
  const onSubmit = (e) => {
    // TODO: add form validation
    e.preventDefault();
    console.log(e);
    login(formData)
      .then((r) => {
        console.log(r);
        console.log(r.statusCode);
        setResponse({ ...response, result: r });
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
      {response.result && <div>{response.result}</div>}
    </div>
  );
};

export default LoginScreen;