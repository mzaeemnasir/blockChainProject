import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Switch } from 'react-router-dom';
import App from './App';
import App2 from './App2';

function RoutePage() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route exact path="/" component={App} />
                    <Route exact path="/app" component={App2} />
                </Switch>
            </div>
        </Router>
    );
}

export default RoutePage;
