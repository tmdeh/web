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
    let schoolInfo = new Object;

    console.log(jsonbody.schoolInfo[1].row[0]);
    for(let i = 0; jsonbody.schoolInfo[1].row[i] =! undefined; i++){
      let schoolCode = jsonbody.schoolInfo[1].SD_SCHUL_CODE
      let schoolName = jsonbody.schoolInfo[1].SCHUL_NM
      console.log(schoolName);

      schoolInfo.schoolCode = schoolCode;
      schoolInfo.schoolName = schoolName;
    }

    console.log(schoolInfo);
    res.status(200).json({});
    });
});

router.get('/:schhool/meal', (req, res, next) => {

});

module.exports = router;
