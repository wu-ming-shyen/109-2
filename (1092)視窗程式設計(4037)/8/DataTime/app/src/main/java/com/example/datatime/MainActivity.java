package com.example.datatime;

import androidx.appcompat.app.AppCompatActivity;

import android.app.DatePickerDialog;
import android.app.TimePickerDialog;
import android.os.Bundle;
import android.view.View;
import android.widget.DatePicker;
import android.widget.TextView;
import android.widget.TimePicker;

import java.util.Calendar;

public class MainActivity extends AppCompatActivity implements View.OnClickListener,DatePickerDialog.OnDateSetListener,TimePickerDialog.OnTimeSetListener {

    Calendar c = Calendar.getInstance();
    TextView txDate;
    TextView txTime;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        txDate = (TextView)findViewById(R.id.textView1);
        txTime = (TextView)findViewById(R.id.textView2);
        txDate.setOnClickListener(this);
        txTime.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        if(view == txDate){
            new DatePickerDialog(this,this,c.get(Calendar.YEAR),c.get(Calendar.MONTH),c.get(Calendar.DAY_OF_MONTH)).show();
        }
        else if(view == txTime){
            new TimePickerDialog(this,this,c.get(Calendar.HOUR_OF_DAY),c.get(Calendar.MINUTE),true).show();
        }
    }

    @Override
    public void onDateSet(DatePicker view, int y, int m, int d) {
        txDate.setText("日期:" + y + "/" + (m+1) + "/" + d);
    }

    @Override
    public void onTimeSet(TimePicker view, int h, int m) {
        txTime.setText("時間:" + h + ":" + m);
    }
}