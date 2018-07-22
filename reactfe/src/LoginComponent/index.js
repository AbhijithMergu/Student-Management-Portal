import React, {Component} from 'react';

class LoginComponent extends Component{

    state={ name : '', password : ''};

    saveName = (event ) => {
        const {target:{value}} = event;
        this.setState({
            password:value
        })
    }

    savePassword = (event) =>{
        const {target:{value}} = event;
        this.setState({
            name:value
        })
    }

    submit = (event) =>{
        const {name,password} = this.state;

        fetch('http://127.0.0.1:8000/api/api-token-auth/', {
            method: 'post',
            headers:{
                "Content-Type": "application/json"
            },
             body: JSON.stringify({ username: name, password: password })

        }).then(token => (token.json())).then(
            tokenJson =>{
                console.log(tokenJson['token'])
            }
        )
    };

    render(){
        return (
            <div>
                <input onChange={this.saveName} name="name"/>
                <br/>
                <input onChange={this.savePassword} name="pass"/>
                <br/>
                <button onClick={this.submit}>Submit</button>
                <br/>
            </div>
        )


    }

}

export default LoginComponent;