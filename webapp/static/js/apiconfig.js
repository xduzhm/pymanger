layui.define(function (exports) {

    const baseUrl = '/api/';
    const apiconfig = {
        user: {
            login: baseUrl + 'user/login',
            getUsers: baseUrl + 'user/getusers',
            getMenus: baseUrl + 'getmenus',
        }
    };
    exports('apiconfig', apiconfig);
});