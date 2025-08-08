package com.example;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;

import org.json.JSONArray;
import org.json.JSONObject;

public class Main {

    public static String HashToString(Map<Integer, String> hashmap){
        String joineStrings = String.join(", ", hashmap.values());
        //System.out.println(" sentences " + joineStrings + " ---------- ");
        return joineStrings;
    }

    public static Map<String, Double> ApiTest(String _uri, String _bodyReq){
        HttpClient  client   = HttpClient.newHttpClient();
        HttpRequest request  = HttpRequest.newBuilder().uri(URI.create(_uri))
        .header("Content-Type", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(_bodyReq, StandardCharsets.UTF_8))
        .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            JSONArray jsonArray           = new JSONArray(response.body());
            Map<String, Double> recommenderHashMap = new HashMap<>();
            jsonArray.forEach(item ->{
                JSONArray itemArray = (JSONArray) item;
                String  key         = itemArray.getString(0);
                Double  value       = itemArray.getDouble(1);
                recommenderHashMap.put(key, value);
            });
            //recommenderHashMap.forEach((k, v) -> System.out.println(k + v));
            return recommenderHashMap;

        } catch (Exception e) {
            System.out.println("Error: "+ e);
            
        }
        return null;
    }
    public static void main(String[] args) {
        Map<Integer, String> hashBodyReq = new HashMap<>();
        hashBodyReq.put(1, "Conversão Automática de Arquivos PDF para Texto com AWS Lambda e Amazon Textract");
        hashBodyReq.put(2, "Integração de API REST com AWS Lambda para Gerenciamento de Usuários");
        hashBodyReq.put(3, "Monitoramento de Logs de Aplicação com Lambda e Envio de Alertas");

        String bodyReq                     = HashToString(hashBodyReq);
        Map<Integer, String> hashBodyReq02 = new HashMap<>();
        hashBodyReq02.put(1, bodyReq);

        JSONObject jsonObj = new JSONObject(hashBodyReq02);
        String bodyReqJson = jsonObj.toString();

        String uri = "http://127.0.0.1:5000/sendSearches";

        Map<String, Double> result = ApiTest(uri, bodyReqJson);
        System.out.println(result);
    }
}