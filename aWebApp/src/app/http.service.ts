import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  serviceUrl: string = ''

  check: object;
  postId: object;
  first: string = 'http://34.69.143.117:8000/stockinfo/?s=';
  second: string = '&r=5d&i=1d'

  constructor(private http: HttpClient) { }

  search(stockname: string) {
    this.http.get<any>(this.first + stockname + this.second, { 'headers': { 'content-type': 'application/json' } }).subscribe(data => {
    this.postId = data.status;
    console.log(data);    
    })

    console.log(stockname);
    
    return this.postId === undefined;
  }

  getInfo() {

  }

}
