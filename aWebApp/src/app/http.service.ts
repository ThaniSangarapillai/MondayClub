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
  storeName: string = '';
  constructor(private http: HttpClient) { }

  search(stockname: string) {
    console.log(stockname);
    
    this.storeName = stockname;
    return this.http.get<any>(this.first + stockname + this.second, { 'headers': { 'content-type': 'application/json' } });   
  }

  public getstocks() : any {
    //returnData: Object;

    return this.http.get('http://34.69.143.117:8000/getmassinfo/', { 'headers': { 'content-type': 'application/json' } });
  }

  getInfo() {
    return this.http.get<any>(this.first + this.storeName + this.second, { 'headers': { 'content-type': 'application/json' } });
  }

}
