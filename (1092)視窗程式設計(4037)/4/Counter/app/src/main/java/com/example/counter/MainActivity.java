package com.example.counter;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity
        implements View.OnClickListener,View.OnLongClickListener{

    int count = 0;
    TextView t;
    Button b;
    /*
        class MyOnClickListener implements View.OnClickListener{
            public void onClick(View v){
                t.setText(String.valueOf(++count));
            }
        }

        MyOnClickListener ClickListener = new MainActivity.MyOnClickListener();
    */
/*
    class MyOnLongClickListener implements View.OnLongClickListener{
        public boolean onLongClick(View v) {
            if(v.getId() == R.id.T){
                count = 0;
                t.setText("0");
            }
            else{
                count+=2;
                t.setText(String.valueOf(count));
            }
            return true;
        }
    }
    MyOnLongClickListener LongClickListener = new MyOnLongClickListener();
*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        t = (TextView) findViewById(R.id.T);
        b = (Button) findViewById(R.id.B);
        b.setOnClickListener(this);
        t.setOnLongClickListener(this);
        b.setOnLongClickListener(this);

        //b.setOnClickListener(ClickListener);
        //t.setOnLongClickListener(LongClickListener);
        //b.setOnLongClickListener(LongClickListener);
/*
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                t.setText(String.valueOf(++count));
            }
        });
        t.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View v) {
                count = 0;
                t.setText("0");
                return false;
            }
        });
        b.setOnLongClickListener(new View.OnLongClickListener() {
            @Override
            public boolean onLongClick(View v) {
                count+=2;
                t.setText(String.valueOf(count));
                return false;
            }
        });
*/
    }

    @Override
    public void onClick(View v) {
        t.setText(String.valueOf(++count));
    }


    @Override
    public boolean onLongClick(View v) {
        if(v.getId() == R.id.T){
            count = 0;
            t.setText("0");
        }
        else{
            count+=2;
            t.setText(String.valueOf(count));
        }
        return true;
    }

}