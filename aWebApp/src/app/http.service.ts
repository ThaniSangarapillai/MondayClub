import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  serviceUrl: string = ''

  check: object;
  postId: object;


  constructor(private http: HttpClient) { }

  search(stockname: string) {
    this.http.post<any>('http://34.69.143.117:8000/stockinfo/', [{ "stock": "MSFT", "range": "5d", "interval": "1d" }], {'headers':{ 'content-type': 'application/json'}}).subscribe(data => {
    this.postId = data.id;
    console.log(data);    
  })

  console.log(name);
  

  return true;  
    
  }

  getInfo() {
    
  }

}
