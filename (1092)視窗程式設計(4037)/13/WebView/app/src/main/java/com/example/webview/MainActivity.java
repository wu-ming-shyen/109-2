package com.example.webview;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.ProgressBar;

public class MainActivity extends AppCompatActivity {

    WebView wv;
    ProgressBar pb;

    @Override
    public void onBackPressed(){
        if(wv.canGoBack()){
            wv.goBack();
            return;
        }
        super.onBackPressed();
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        wv = (WebView) findViewById(R.id.wv);
        wv.setWebViewClient(new WebViewClient());
        wv.getSettings().setJavaScriptEnabled(true);
        wv.loadUrl("https://www.google.com/");
        pb = (ProgressBar)findViewById(R.id.pb);
        wv.setWebChromeClient(new WebChromeClient(){
            public void onProgressChanged(WebView view,int progress){
                pb.setProgress(progress);
                pb.setVisibility(progress<100?view.VISIBLE:view.GONE);
            }
        });
    }
    public void onClick(View view){
        if (view.getId()==R.id.button1){
            wv.loadUrl("https://wp.npust.edu.tw/");
        }
        if (view.getId()==R.id.button2){
            wv.loadUrl("https://www.youtube.com/");
        }
    }
}