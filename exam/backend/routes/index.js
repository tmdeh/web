var express = require('express');
var router = express.Router();
const request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('../public/index.html');
});

router.get('/:schoolName', (req, res, next) => {
  const school = req.params.schoolName;
  let url = "https://open.neis.go.kr/hub/schoolInfo?KEY=f08d52196c3a48ecbd679177083b65f0&Type=json&SCHUL_NM=" + encodeURI(school);
  request(url, (err, response, body) => {
    if(err){
      return res.status(400).json({err});
    }
    let jsonbody = JSON.parse(body); //json으로 파싱
    if(jsonbody.schoolInfo == undefined){
      res.status(200).json({});
      return;
    }
    let school = jsonbody.schoolInfo[1]
    let schoolcode = school.row[i].SD_SCHUL_CODE;
    res.redirect('/:school/meal', schoolcode);
    });
});

router.get('/:schhool/meal', (req, res, next) => {

});

module.exports = router;
