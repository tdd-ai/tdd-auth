import React, { useState } from "react";
import { signUp } from "../services/AuthService";
const SignUpScreen = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    first_name: "",
    last_name: null,
    affiliation: null,
  });
  const [response, setResponse] = useState({ result: null, error: null });
  const handleChange = (e) => {
    setFormData({
      ...formData,

      // Trimming any whitespace
      [e.target.name]: e.target.value.trim(),
    });
  };
  const onSubmit = (e) => {
    // TODO: add form validation
    e.preventDefault();
    console.log(e);
    signUp(formData)
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
          <h3>Sign Up</h3>

          <div className="form-group">
            <label>Email address *</label>
            <input
              name="email"
              type="email"
              className="form-control"
              placeholder="Enter email"
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>First Name *</label>
            <input
              name="first_name"
              type="text"
              className="form-control"
              placeholder="Enter your name"
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Last Name</label>
            <input
              type="text"
              name="last_name"
              className="form-control"
              placeholder="Enter your last name"
              onChange={handleChange}
            />
          </div>

          <div className="form-group">
            <label>Password *</label>
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
              formData.email && formData.password && formData.first_name
                ? "btn btn-primary btn-block"
                : "disabled-btn btn btn-primary btn-block "
            }
            disabled={
              !formData.email || !formData.password || !formData.first_name
            }
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
            return response.error[keys[0]][0];
          })()}
        </div>
      )}
      {response.result && <div>{response.result}</div>}
    </div>
  );
};

export default SignUpScreen;
