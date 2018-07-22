import React,{Component} from 'react';

import './styles.css';

class HeaderComponent extends Component{

    state = {
        loggedIn : this.props.loggedIn
    };

    toggleUserState = () =>{
        this.setState(prev => ({loggedIn: !prev.loggedIn}))
    };

    render(){
            const {title} = this.props;
            const {loggedIn} = this.state;
        return(
            <div className="header">
                <h2>{title}</h2>
                <div className="menu" onClick={this.toggleUserState}>
                    { loggedIn?<span>Login</span>:<span>Logout</span> }
                </div>
            </div>
        )
    }
}

export default HeaderComponent;