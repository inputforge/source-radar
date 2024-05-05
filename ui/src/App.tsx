import {RouterProvider} from "react-router-dom";
import router from "./routes.tsx";

function App() {
    return (
        <RouterProvider router={router} fallbackElement={<div>Loading...</div>}/>
    )
}

export default App
