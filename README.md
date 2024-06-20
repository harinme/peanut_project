<h1 align="center">🥜Peanut_project</h1>
<p align="center">
Yolov8 segmentation을 활용한 불량 땅콩 검출
</p>
<h2> Team 도란도란</h2>
  <table align=center>
    <tr align=center width=1000 height=100>
    <td>
      <img src="https://i.imgur.com/CiyBZtG.jpeg">
    </td>  
     <td>
       <img src="https://i.imgur.com/qapqp5E.jpeg">
    </td> 
     <td>
       <img src="https://i.imgur.com/CXVHcO9.jpeg">
    </td> 
     <td>
        <img src="https://i.imgur.com/40ywq5L.jpeg">
    </td> 
     <td>
        <img src="https://i.imgur.com/txjDGop.jpeg">
    </td> 
     <td>
        <img src="https://i.imgur.com/mrU9yzy.jpeg">
    </td> 
    </tr>
    <tr align=center width=1000 height=110>
       <td align=center>
      <h4>임유나</h4>
데이터셋 수집
         <br>
레이블링<br>
         모델링
      </td> 
     <td>
     <h4> 배은영</h4>
레이블링
          <br>
YOLO 재학습
          <br>
코드구현
    </td> 
     <td>
     <h4> 도규림</h4>
데이터셋 수집
          <br>
레이블링
    </td> 
   <td>
     <h4> 임태창</h4>
데이터셋 수집   <br>
레이블링
    </td> 
       <td>
    <h4> 장우진 </h4> 
         YOLO 재학습   <br>
         코드 구현
    </td> 
       <td>
     <h4> 변우성</h4>
         데이터셋 수집
    </td> 
  </table>
  
 
 



</p>

<br>

<h2> 왜 불량 땅콩 검출인가? </h2> 
<p align="center">
<img width=600 src="https://github.com/harinme/peanut_project/assets/152590695/d9a9c063-6ef4-4268-b26b-b3acc90f92de?center=true">
</p>
<p>
  국내 대기업을 중심으로 AI 기반의 불량 검출시스템이 빠르게 적용되고 있다.
  하지만, 중소기업 및 식품 공정 과정에서는 적용 수준이 아직까지는 미비하다고 볼 수 있다.
이에 본 프로젝트에서는 AI와 머신러닝을 활용한 불량 검출의 대중화를 이루는데 초점을 두어 주변에서 쉽게 구할 수 있는 땅콩을 통해서 실험해 보고자 한다.
</p>


<br>

<H2>
  개발 과정
</H2>
<h3>
  개발 환경
</h3>
<p align=center>
 <img width=150 src=https://github.com/harinme/peanut_project/assets/152590695/63a4d7ae-70d3-48f2-bfdf-0c12188d6376">
 <img  width=350 src=https://github.com/harinme/peanut_project/assets/152590695/48b8bf0d-fde2-4158-9bb0-159d9c6b5b6c">
 <img  width=350 src=https://github.com/harinme/peanut_project/assets/152590695/09d0244a-934f-422e-af71-8cfe86a94941">
</p>

<br>

<h3>
  개발 기간
</h3>
  <img src="https://github.com/harinme/peanut_project/assets/152590695/a8142144-a1d4-48e0-972b-9adda3891bbf">

  <br>
  
  <h3>
    요구사항 분석
  </h3>
  <p align=center>
    <img src="https://github.com/harinme/peanut_project/assets/152590695/4ff26bd0-2785-48da-a9cf-cb058750e366">
  </p>
- 컨베이어벨트와 웹캠 셋팅  <br>
- 웹캠으로 실시간 땅콩 이미지 분석 <br>
- 불량 땅콩 검출시 음성 알림 <br>
  </p>
<br>

  <h3>
    장치 설계
  </h3>
  <p align=center>
  <img src="https://github.com/harinme/peanut_project/assets/152590695/6949a066-1f23-49c6-ae06-7b927264bc8d">
  </p>

  <br>

<h3>
  프로젝트 구현
</h3>
  <h4>
    Dataset 수집 및 전처리(Roboflow)
  </h4>
    <p align=center>
  <img width=500 src="https://github.com/harinme/peanut_project/assets/152590695/64e4ba9e-095d-4337-ab64-f09418ea8c2c">
  <img width=500 src="https://github.com/harinme/peanut_project/assets/152590695/6368e95f-1041-4536-8126-d8f31213cc58">
    </p>
  <h4>  
      1차 모델: 불량 땅콩 10장
  </h4>
      <br>
   <h4>
      2차 모델: 불량 땅콩 10장, 정상 땅콩 15장
   </h4>
      <p align=center>
     <img src="https://github.com/harinme/peanut_project/assets/152590695/042d1c62-175f-4954-a0d8-6de7ffcd4bcc">
        <br>
        불량 땅콩 검출이 잘 안됨(conf 낮춰도 동일함) -> 불량 땅콩 데이터셋 추가
    </p>
<br>
  </h4>
      <br>
   <h4>
      3차 모델: 불량 땅콩 40장 추가(약 30개씩)
   </h4>
      <p align=center>
        <img src="https://github.com/harinme/peanut_project/assets/152590695/053b295a-1965-45e9-b802-86c63c55b2b2">
        <br>
        여전히 불량 땅콩 검출이 잘 안됨-> 정상 땅콩 데이터셋 추가
    </p>
    <br>
   <h4>
      4차 모델: 정상 땅콩 10장 추가(약 30개씩)
   </h4>
      <p align=center>
       <img width=400 src="https://github.com/harinme/peanut_project/assets/152590695/82d2ed52-fd87-4a19-af9b-6ac984211808">
       <img width=400  src="https://github.com/harinme/peanut_project/assets/152590695/0bb337bc-34b7-4b39-96a9-4539458f1f02">
        <br>
        고화질에서는 검출이 잘 되지만 저해상도(web-cam)에서는 인식이 안됨-> 저해상도 데이터셋 추가
    </p>
     <br>
   <h4>
      5차 모델(최종): 저해상도 데이터셋 추가
   </h4>
      <p align=center>
   <img src="https://github.com/harinme/peanut_project/assets/152590695/cea6c0f7-56b2-47ab-bdd9-b564b5566ea6">
        <br>
        저해상도에서도 잘 검출함.
    </p>
<h3>프로젝트 결과</h3>


https://github.com/harinme/peanut_project/assets/152590695/93d72469-fbd1-4700-b6e6-9f1da1731dd1


<br>
<h3>향후 발전 방향</h3>
<p>
1. 분류 세분화 - 불량 검출 결과가 정상과 불량 딱 2가지로만 되어있기 때문에 껍질이 붙어있는 정도에 따라서 분류를 세분화하기
  <br>
  
2. 시스템 자동화 - 단순 알림이 아닌 분류 결과에 따라서 자동으로 분리되게 시스템화하기
  <br>
  ex) 바람 분사하는 기계 설치, 땅꽁 나열 후 분류에 따라서 불량은 바람 분사 / 틀에 넣은 후 불량이 들어있는 틀은 떨어지게 함 등
</p>
