var express = require('express');
var router = express.Router();
const request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('../public/index.html');
});

router.get('/api/:schoolName', (req, res, next) => {
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
    // console.log(jsonbody.schoolInfo[1].row[0]);
    let result = [];
    for(let i = 0; jsonbody.schoolInfo[1].row[i] != undefined; i++){
      let schoolCode = jsonbody.schoolInfo[1].row[i].SD_SCHUL_CODE;
      let schoolName = jsonbody.schoolInfo[1].row[i].SCHUL_NM;
      let EOCode = jsonbody.schoolInfo[1].row[i].ATPT_OFCDC_SC_CODE;
      let EOName = jsonbody.schoolInfo[1].row[i].ATPT_OFCDC_SC_NM

      let tmp = new Object();
      tmp.school_code = schoolCode;
      tmp.school_name = schoolName;
      tmp.EOCode = EOCode;
      tmp.EOName = EOName;
      result.push(tmp);
    }

    res.status(200).json(result);
    });
});

router.get('/api/:schhool/meal', (req, res, next) => {

});

module.exports = router;
