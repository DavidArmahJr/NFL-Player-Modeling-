var express = require('express');
var router = express.Router();
const userController = require('../controllers/user.controller');
const Role = require('../_helpers/role');
const authorize = require('../_helpers/authorize');


router.post('/authenticate', userController.authenticate);
router.post('/register', userController.register);
router.post('/registerGym', userController.registerGym);
router.get('/allusers', authorize(Role.trainer),userController.getAllUsers);
router.post('/track',authorize(Role.member),userController.trackProgress);
router.get('/userinfo', authorize(Role.member),userController.getUserInfo);
router.get('/leaderboard',userController.getGymLeaderboards);


module.exports = router;
