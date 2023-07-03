var express = require('express');
var router = express.Router();
const gymController = require('../controllers/gym.controller');
const Role = require('../_helpers/role');
const authorize = require('../_helpers/authorize');


router.post('/addgyms', authorize(Role.trainer), gymController.createGyms);
router.get('/getgyms', gymController.getGyms);
router.delete('/:id',authorize(Role.trainer), gymController.deleteGyms);



module.exports = router;
