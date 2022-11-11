#une partie du code de maching pour les données venant d'Elasticsearch(base de données No sql)
#le code de maching va déduire un score entre le candidat et l'offre d'emploi ,il va prendre en compte la Localisation ,les compétences et le nombre d'éxperiences 
import json
import time
from elasticsearch import Elasticsearch ,exceptions # ...   
from elasticsearch_repo import *   
from flask import Flask, jsonify, request,make_response, abort

from flask_cors import CORS,cross_origin

# Matching profiles by jobs
#j'ai crée une WEB Service (API) qui permet d'effectuer la réquete HTTP POST
@app.route('/api/v1/jobs/matching/<jobs_id>', methods=['POST'])
def getoffreprofil(jobs_id):  

    res_job = searchDocById(index='offre', id=jobs_id) 
    print(res_job)
    if res_job != {} : 
     #  results = es.get(index='offre',  id=jobs_id)
       print(res_job['skills'].split(','))
       Required_skills=res_job['skills'].split(',')
       seniority_years_interval=res_job['seniority']       
       print(seniority_years_interval)
      # location = res_job['location'] 
       
       if (seniority_years_interval==0 ):
        seniority_years_interval_from=seniority_years_interval*12
       else:
        seniority_years_interval_from=seniority_years_interval*12-12
       print('==========')
       body = { 
     
        "query": {
          "bool": {
            "should": [],
            "minimum_should_match" :1 ,
            "filter": [
              {"range": { "diffMonth": { "gte":seniority_years_interval_from }}} ,  
            
              ]}},"fields": [{"field": "diffMonth"}]}
       req_body = body['query']['bool'] 
       for i in range(len(Required_skills)):
       #  req_body['should'].append(  { "constant_score": { "filter": { "match_phrase": {"experiences.tasks": {"query":Required_skills[i]  }} }, "boost": (1/len(Required_skills))*100}},)  
        req_body['should'].append({"constant_score":{"filter":{"multi_match":  {"query":Required_skills[i],"fields":["experiences.tasks","skills"],"type":"phrase"}}    #,"boost": (1/len(Required_skills))*100
        }}),  
