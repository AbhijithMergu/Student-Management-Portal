import React,{Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class FetchComponent extends Component{

    state = {
        data: null
    };

    componentDidMount() {
        fetch('http://127.0.0.1:8000/api/api-token-auth/', {
            method: 'post',
            headers:{
                "Content-Type": "application/json"
            },
             body: JSON.stringify({ username: "abhijith", password: "abhijith" })
        }).then(token => (token.json())).then(
            token_json => {
                fetch('http://127.0.0.1:8000/api/colleges/', {
                    method: 'get',
                    headers: new Headers({
                        'Authorization': 'JWT ' + token_json["token"],
                    })
                }).then(results => {
            return results.json();
        }).then(resultsJson => this.setState({data: resultsJson}))})

    }
    render(){
        return (
            <div className="container">
                <h2>College List</h2>
                <table className="table table-hover table-bordered ">
                <thead>
                    <tr>
                        <th>Acronym</th>
                        <th>Name</th>
                        <th>Location</th>
                        <th>Contact</th>
                    </tr>
                </thead>
                <tbody>
                {

                    this.state.data && this.state.data.map(
                        college => (
                            <tr key = {college.id}>
                                 <td> {college.acronym }</td>
                                <td><Link to={"/app/college/"+college.id+"/"}>{college.name}</Link></td>
                                <td> {college.location}</td>
                                <td> { college.contact} </td>

                            </tr>
                        ))
                }
                </tbody>
                </table>

                <ul><li><Link to='/app/college/1/'>LGo to login </Link></li></ul>
            </div>
        )
    }
}

export default FetchComponent;