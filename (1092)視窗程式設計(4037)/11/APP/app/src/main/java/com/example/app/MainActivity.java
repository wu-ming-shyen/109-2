package com.example.app;

import androidx.appcompat.app.AppCompatActivity;

import android.app.SearchManager;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    public void onClick(View view){
        Intent it = new Intent(Intent.ACTION_VIEW);
        switch (view.getId()){
            case R.id.imageButton1:
                it.setData(Uri.parse("mailto:michell891012@gmail.com?cc=B10856012@mail.npust.edu.tw&subject=Hello World!&body=Congratulations! You are successful."));
                break;
            case R.id.imageButton2:
                it.setData(Uri.parse("sms:0918-928-733?body=您好!"));
                break;
            case R.id.imageButton3:
                it.setData(Uri.parse("https://wp.npust.edu.tw/"));
                break;
            case R.id.imageButton4:
                it.setData(Uri.parse("geo:22.64111,120.59611"));
                break;
            case R.id.imageButton5:
                it.setAction(Intent.ACTION_WEB_SEARCH);
                it.putExtra(SearchManager.QUERY,"劉寧漢老師");
                break;
        }
        startActivity(it);
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}