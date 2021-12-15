const StorageKeys = {
  accessToken: "accessToken",
  refreshToken: "refreshToken",
  firstName: "first_name",
  lastName: "last_name",
  email: "email"
};

const saveAccessToken = (accessToken) => {
  localStorage.setItem(StorageKeys.accessToken, accessToken);
};

const saveRefreshToken = (refreshToken) => {
  localStorage.setItem(StorageKeys.refreshToken, refreshToken);
};

const saveFullName = (firstName, lastName) => {
  localStorage.setItem(StorageKeys.firstName, firstName)
  localStorage.setItem(StorageKeys.lastName, lastName)
}

const getAccessToken = () => {
  localStorage.getItem(StorageKeys.accessToken);
};

const getRefreshToken = () => {
  localStorage.getItem(StorageKeys.refreshToken);
};


const StorageService = {
  StorageKeys,
  saveAccessToken,
  saveRefreshToken,
  saveFullName,
  getAccessToken,
  getRefreshToken,
};

export default StorageService;
