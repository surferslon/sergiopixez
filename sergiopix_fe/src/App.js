import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import PostList from './Pages/PostList';
import PostDetails from './Pages/PostDetails';
import Admin from './Pages/Admin';


function App() {
  return (
    <Router>
      <Route exact path="/" component={PostList}/>
      <Route path="/post/:id" component={PostDetails}/>
      <Route path="/admin/" component={Admin}/>
    </Router>
  );
}

export default App;
