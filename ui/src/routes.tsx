import {createBrowserRouter, Navigate} from "react-router-dom";
import Layout from "@/pages/Layout.tsx";
import Projects from "@/pages/Projects.tsx";
import {api, query} from "@/lib/client.ts";
import Settings from "@/pages/Settings.tsx";

const router = createBrowserRouter([{
        element: <Layout/>,
        children: [
            {
                path: "/",
                element: <Navigate to="/projects"/>,
            },
            {
                path: "/projects",
                element: <Projects/>,
                loader: () => query("projects", async () => {
                    return await api("GET", "/projects");
                }),
            },
            {
                path: "/settings",
                element: <Settings/>,
            }
            // {
            //     path: "/projects/:projectId",
            //     element: <Project/>,
            // }
        ]
    }]
);

export default router