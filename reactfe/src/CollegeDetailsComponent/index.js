import React,{Component} from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class CollegeDetailsComponent extends Component{

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
                fetch('http://127.0.0.1:8000/api/colleges/'+this.props.match.params.id+'/students/', {
                    method: 'get',
                    headers: {
                        'Authorization': 'JWT ' + token_json["token"],
                    }
                }).then(results => {
            return results.json();
        }).then(resultsJson => this.setState({data: resultsJson}))})

    }
    render(){
        return (
            <div className="container">
                <h2>Student List</h2>
                <table className="table table-hover table-bordered ">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Email</th>
                        <th>DB FOLDER</th>
                    </tr>
                </thead>
                <tbody>
                {

                    this.state.data && this.state.data.map(
                        student => (
                            <tr key = {student.id}>
                                 <td> {student.name }</td>
                                 <td>{student.email}</td>
                                <td> {student.db_folder}</td>

                            </tr>
                        ))
                }
                </tbody>
                </table>

                <ul><li><Link to='/app/login/'>Go to login </Link></li></ul>
            </div>
        )
    }
}

export default CollegeDetailsComponent;