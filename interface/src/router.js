import Vue from "vue";
import Router from "vue-router";
// add components
import About from "./views/About"
import Main from "./views/Main"
import Login from "./views/auth/Login"
import Register from "./views/auth/Register"
import List from "./views/List"
import View from "./views/View"
import Average from "./views/Average"
import Rate from "./views/Rate"


Vue.use(Router);

// 라우터 정의하기
const router = new Router({
    mode: "history",
    // 이부분만 컴포넌트가 바뀌게 하는것 
    routes: [
        {
            path: "/",
            name: "main",
            component: Main
        },
        {
            path: "/about",
            name: "about",
            component: About
        },
        {
            path: "/login",
            name: "login",
            component: Login
        },
        {
            path: "/register",
            name: "register",
            component: Register
        },
        {
            path: "/list",
            name: "list",
            component: List
        },
        {
            path: "/view",
            name: "view",
            component: View
        },
        {
            path: "/average",
            name: "average",
            component: Average
        },
        {
            path: "/rate",
            name: "rate",
            component: Rate
        },


    ]
})



export default router;
