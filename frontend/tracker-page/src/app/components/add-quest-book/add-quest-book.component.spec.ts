import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddQuestBookComponent } from './add-quest-book.component';

describe('AddQuestBookComponent', () => {
  let component: AddQuestBookComponent;
  let fixture: ComponentFixture<AddQuestBookComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddQuestBookComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AddQuestBookComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
