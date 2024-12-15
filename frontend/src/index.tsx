import React, { StrictMode } from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
// import { UserProvider } from './components/UserContext'

const router = createBrowserRouter([
    {
        path: '/',
        element: <App />,
    },
]);

const container = document.getElementById('app');
const root = ReactDOM.createRoot(container!);
root.render(
    <StrictMode>
        {/* <UserProvider>            */}
            <RouterProvider router= {router} />     
        {/* </UserProvider> */}
    </StrictMode>
);
