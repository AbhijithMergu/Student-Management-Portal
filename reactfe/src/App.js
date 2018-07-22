import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import './HeaderComponent/styles.css'
import HeaderComponent from "./HeaderComponent";
import FetchComponent from "./FetchComponent";
import LoginComponent from "./LoginComponent"
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import CollegeDetailsComponent from "./CollegeDetailsComponent";
import StudentDetailsComponent from "./StudentDetailsComponent";


class App extends Component {
  render() {
    return (
      <div className="App">

          <HeaderComponent title="Mentor App" loggedIn ={false}/>
          <br/><br/>
        {/*<header className="App-header">*/}
          {/*<img src={logo} className="App-logo" alt="logo" />*/}
          {/*<h1 className="App-title">Welcome to React</h1>*/}
        {/*</header>*/}
          {/*<FetchComponent/>*/}
          {/*<LoginComponent/>*/}
        {/*<p className="App-intro">*/}
          {/*To get started, edit <code>src/App.js</code> and save to reload.*/}
        {/*</p>*/}

        <Router>
          <React.Fragment>
            <Route exact path='/app/' component={FetchComponent}/>
            <Route exact path='/app/login/' component={LoginComponent}/>
              <Route exact path='/app/college/:id/' component={CollegeDetailsComponent}/>
              <Route exact path='/app/college/:college_id/:id/' component={StudentDetailsComponent}/>
              <Route/>
          </React.Fragment>
        </Router>
      </div>
    );
  }
}

export default App;
