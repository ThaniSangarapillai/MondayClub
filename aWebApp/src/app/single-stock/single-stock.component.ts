import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-single-stock',
  templateUrl: './single-stock.component.html',
  styleUrls: ['./single-stock.component.scss']
})
export class SingleStockComponent implements OnInit {

  name: string = 'Mo vs Thani';

  constructor() { }

  ngOnInit(): void {
  }

}
